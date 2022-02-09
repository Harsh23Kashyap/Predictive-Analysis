log <- function(msg) {
  print(msg)
  write(msg, file = "log.txt", append = TRUE)
}


help <- function() {
  print("Allowed syntax :-")
  print("Rscript file.r <input>.csv")
}

args <- commandArgs(trailingOnly = TRUE)
print(args)

if (length(args) != 1) {
  help()
  stop("Invalid Syntax")
} else {
  if (!file.exists(args[1])) {
    stop("File Not Exists")
  }
}


#IMPORTING LIBRARIES
library(Peptides)
library(peptider)

#SET WORKING DIRECTORY
setwd("/Users/licious/Downloads/Thapar/Predictive Analysis")
print("Current Working Directory - ")
print(getwd)
input_file <- args[1]
data <- read.csv(input_file)
print(data)

log("Making features for all")
df$lengthpep <- lapply(df$Peptide.Sequence, lengthpep)
df$a_index <- lapply(df$Peptide.Sequence, aIndex)
df$boman <- lapply(df$Peptide.Sequence, boman)
df$charge <- lapply(df$Peptide.Sequence, charge)
df$instaIndex <- lapply(df$Peptide.Sequence, instaIndex)
df$hydrophobicity <- lapply(df$Peptide.Sequence, hydrophobicity)
df$m_w <- lapply(df$Peptide.Sequence, mw)
df$m_z <- lapply(df$Peptide.Sequence, mz)
df$codons <- lapply(df$Peptide.Sequence, codons, libscheme = "NNK")
df$no_of_Neighbors <- lapply(df$Peptide.Sequence, getNofNeighbors)
df$ppeptide <- lapply(df$Peptide.Sequence, ppeptide, libscheme = "NNK", N = 10^8)
df$z_scales <- lapply(df$Peptide.Sequence, zScales)

df$z_scales <- lapply(df$z_scales, function(x) x[[1]])
log("Made features")

flatten <- function(l) {
  if (!is.list(l)) {
    l
  } else {
    do.call("rbind", lapply(l, function(x) `length<-`(x, max(lengths(l)))))
  }
}

df[] <- lapply(df, flatten)
log("flatten df")

filename <- "output.csv"
write.csv(df, filename, row.names = FALSE)
log(paste("wrote in", filename))