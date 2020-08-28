program loop
integer i, n, sum 
n = 5
sum = 0
do i=1, n
    sum = sum+i
    write(*,*) 'i=', i
    write(*,*) 'sum=', sum
end do
stop
end