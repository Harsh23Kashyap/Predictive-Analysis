#To write in file 
#Create a new file . Dont append
write("Program Started\n Harsh Kashyap\n101917088\nThapar Institute", file = "log-101917088.txt", append = FALSE)


log <- function(msg) 
{
  write(msg, file = "log.txt", append = TRUE)
}


help <- function() 
{
  print("Allowed syntax :-")
  print("Rscript file.r <input>.csv")
}

args <- commandArgs(trailingOnly = TRUE)
print(args)

if (length(args) != 1) 
{
  help()
  log("Invalid Syntax")
  stop()
} else 
{
  if (!file.exists(args[1])) 
  {
    log("File Not Exists")
    stop()
  }
}


#install.packages('Peptides')
#install.packages('peptider')

#IMPORTING PACKAGES
library('Peptides')
library('peptider')

input = commandArgs(trailingOnly=T)
myData = read.csv(input[1])


rowNames=myData[,1]
rowNames <- c("", rowNames)

i=0
log("Making features")
for( i in 1:length(myData[,1]))
{
  sequence <- myData[i,1]
  tar <- myData[i,2]
  names(sequence) <- "Peptide Sequence"
  names(tar) <- "Target"
  #F1 Aliphatic index
  f1 <- aIndex(sequence)
  
  #F2 Boman Index
  f2 <- boman(sequence)
  
  #F3 Insta Index
  f3 <- instaIndex(sequence)
   
  #F4
  f4 <- ppeptide(sequence, libscheme = "NNK", N=10^8)
  resultPart1 <- data.frame(f1, f2, f3, f4);
  colnames(resultPart1)  = c("aIndex", "boman", "instaIndex", "ppeptide")
  
  #F5
  f5_1 <- hmoment(seq = sequence, angle = 100, window = 11)
  f5_2 <- hmoment(seq = sequence, angle = 160, window = 11)
  
  #F6
  f6_1 <- mw(seq = sequence, monoisotopic = FALSE)
  f6_2 <- mw(seq = sequence, monoisotopic = TRUE)
  resultPart2 <- data.frame(f5_1, f5_2, f6_1, f6_2)
  colnames(resultPart2)  = c("hmoment_1", "hmoment_2", "molecularWeight_1", "molecularWeight_2")
  
  #F7
  pKscale = c("Bjellqvist", "Dawson", "EMBOSS", "Lehninger", "Murray", "Rodwell", "Sillero", "Solomon", "Stryer")
  f7 <- c()
  for (j in 1:length(pKscale))
  {
    x = charge(seq = sequence, pH = seq(from = 5, to = 9, by = 2), pKscale = pKscale[j])
    f7 <- c(f7, x)
  }
  names(f7) <- paste("charge_", c(1:length(f7)), sep='')
  
  #F8
  scale <- c("Aboderin", "AbrahamLeo", "Argos", "BlackMould", "BullBreese", "Casari", "Chothia", "Cid", "Cowan3.4", "Cowan7.5", "Eisenberg", "Engelman", "Fasman", "Fauchere", "Goldsack", "Guy", "HoppWoods", "Janin", "Jones", "Juretic", "Kidera", "Kuhn", "KyteDoolittle", "Levitt", "Manavalan", "Miyazawa", "Parker", "Ponnuswamy", "Prabhakaran", "Rao", "Rose", "Roseman", "Sweet", "Tanford", "Welling", "Wilson", "Wolfenden", "Zimmerman", "interfaceScale_pH8", "interfaceScale_pH2", "octanolScale_pH8", "octanolScale_pH2", "oiScale_pH8", "oiScale_pH2")
  f8 <- c()
  for( j in 1:length(scale))
  {
    x=hydrophobicity(seq = sequence, scale = scale[j])
    f8 <- c(f8, x)
  }
  names(f8) <- paste("hydrophobicity_", c(1:length(f8)), sep='')
  
  #f9
  pKscale <- c( "Bjellqvist", "EMBOSS", "Murray", "Sillero", "Solomon", "Stryer", "Lehninger", "Dawson", "Rodwell")
  f9<-c()
  for(j in 1:length(pKscale))
  {
    x = pI(sequence, pKscale= pKscale[j])
    f9 <- c(f9, x)
  }
  names(f9) <- paste("pI_", c(1:length(f9)), sep='')

  resultPart3 <- c(f7, f8, f9)
  
  finalResult<- c(sequence, resultPart1, resultPart2, resultPart3, tar)
  if(i==1)
    write.table(finalResult, "output-101917088.csv", sep = ",", row.names=F, col.names = T, append=F)
  else
    write.table(finalResult, "output-101917088.csv", sep = ",", row.names=F, col.names = F, append=T)
}

log("Made features")
log("Written in file: 'output-101917088.csv'")

cat("DONE")