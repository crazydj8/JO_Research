%Calculation of the transponse of the reduced matrix elements
%Part 1 - U^2 values input - input from low to high energy
x=0; %U(n)^2 matrix
q=0;%number of transitions
prompt = 'number of transitions '
q = input(prompt);

for a=1:1:q
 prompt = 'U2 ';
    x(a,1)=input(prompt);
    prompt = 'U4 ';
    x(a,2)=input(prompt);
    prompt = 'U6 ';
    x(a,3)=input(prompt);
end

%Part 2- transpose matrix x
xt=0;
xt=x.';

%Part 3 - transpose * original
p=0;%product xt * x
p = xt*x;

%Part 4 - inverse of p
ip=0;
ip= inv(p);

%Part 5 - ip * xt
f = ip*xt;
