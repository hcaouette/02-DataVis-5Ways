make_graph <- function(){
  library("ggplot2")
  print("helloworld")
  setwd("C:/Users/Hunter/Documents/github/480X_forks/02-DataVis-5Ways")
  cars = read.csv("./cars-sample.csv")
  #print(cars)
  #aes_cars <-
  ggplot(cars_sample, aes(x=Weight, y=MPG, color=Manufacturer)) + geom_point(aes(alpha=0.5,size=Weight))
}

make_graph()
