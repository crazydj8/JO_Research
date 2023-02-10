q=4;
n=0;
for n = 1:1:q
 prompt = 'J value at ground state ';
 y(n,1)=input(prompt);
 prompt = 'Integrated absorption cross section in *10^20 cm^2 ';
 y(n,2)=input(prompt);
 prompt = 'Average wavelentgth of absorption ';
 y(n,3)=input(prompt);
 prompt = 'Refractive index at average wavelength ';
 y(n,4)=input(prompt);
 y(n,5)= y(n,2)*10.41*y(n,4)*(3/(y(n,4)^2+2))^2*(1+2*y(n,1))/y(n,3);
end
    %y(1,5) is the calculated          
    
    
    
    
    