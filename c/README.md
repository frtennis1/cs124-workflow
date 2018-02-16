C
=

In C, the standard compiler to use is GCC. Given a file `prog.c` (with no 
dependencies other than system libraries) you can compile it on the 
command-line into an executable prog by running `gcc prog.c -o prog`. If 
you want your compiler to optimize the assembly it produces, then you can 
pass the `-O1`, `-O2`, or `-O3` flags (but make sure that you have no 
undefined behavior in your program, as this may cause you significant 
confusion). 

As for debugging C programs, it is useful to learn to use a debugger such as 
[GDB](https://www.gnu.org/software/gdb/) in order to determine the cause of 
memory errors such as null pointer dereferences. In order to test your 
programs on sample local test cases, the most straightforward approach is 
likely to read from standard in and write to standard out (using library 
functions such as `scanf` and `printf`, respectively), and accordingly 
redirecting standard in and standard out to and from a file using `<` and `>`. 
That way, you can automate and produce your tests using a higher-level 
language such as bash or python-- it’s likely not worth your while to carry 
out such tasks in C, as it not very important that your testing procedures 
run at the blazing-fast speed of C. 
