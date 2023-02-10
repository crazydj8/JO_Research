%calc of rms error

n=0;
rms = 0;
tot=0;
for n=1:1:q
    tot = tot+y(n,5)^2
end
n=0;
for n=1:1:q
    rms = rms + ((tls(1,n)-y(n,5))^2/tot)^0.5
end