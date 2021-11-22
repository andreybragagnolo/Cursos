media=100; dp=15

lb= min(dataset$Pesos) 
ub=max(dataset$Pesos)  

x <- seq(-4,4,length=100)*dp + media
hx <- dnorm(x,media,dp)

plot(x, hx, type="n", xlab="Probabilidade", ylab="",
     main="Distribuição Normal", axes=FALSE)

i = x >= lb & x <= ub
lines(x, hx)
polygon(c(lb,x[i],ub), c(0,hx[i],0), col="blue")

area <- pnorm(ub, media, dp) - pnorm(lb, media, dp)
result <- paste("P(",lb,"< Peso <",ub,") =",
                signif(area, digits=3))

mtext(result,3)
axis(1, at=seq(40, 160, 20), pos=0)