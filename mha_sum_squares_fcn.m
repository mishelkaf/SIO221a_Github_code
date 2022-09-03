function fs=mha_sum_squares_fcn(n)
%function fs=mha_sum_squares_fcn(n)
%For an input n, return a vector of the sum of the first c squares, up to n.
%8/1/2022 Matthew Alford

c=1;
fs(1)=1.^2;
while c<n
    fs(c+1)=fs(c)+(c+1).^2;
    c=c+1;
end
%fs