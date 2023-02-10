%%Code to calculate A. Make sure to rename the created file every time.
%%Also cancel all the auxiliary variables created so far but q.
clear all;
e=0; q =0; RI = 0; O = 0; Sed = 0;
SumAed = 0; LifeTime = 0; BrRatio = 0;
prompt = 'How many lower transitions?: '; 
q = input(prompt);

promt = 'What is the Refractive Index?: ';
RI = input(promt);

for n = 1:1:3
  prompt = 'Enter the value of JO parameters in order and press enter after each entry: ';
  O(1,n) = input(prompt); 
 end
for n=1:1:q
 prompt = 'J value at excited state ';
    e(n,1)=input(prompt);
   prompt = 'Peak wavelength of emission ';
    e(n,2)=input(prompt);
   prompt = 'Enter U2: ';
    e(n,3)=input(prompt);
   prompt = 'Enter U4: '; 
    e(n,4)=input(prompt);
   prompt = 'Enter U6: '; 
    e(n,5)=input(prompt);
   Sed = e(n,3)*O(1,1)+e(n,4)*O(1,2)+e(n,5)*O(1,3)    
    e(n,6)= 7.23E10*RI*((RI^2+2)/3)^2*Sed/((2*e(n,1)+1)*(e(n,2)*1E-9)^3);
    SumAed = SumAed + e(n,6);
end
% calculation of Life time of states
LifeTime = 1 / SumAed;

% calculation of Branching ratio
for n = 1:1:q
BrRatio(1,n) = e(n,6) / SumAed;
end

%e(n,6) is the calculated Aed ;
%Check if a Amd occurs for the given transition.