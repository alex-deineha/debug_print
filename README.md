# Debug print
<p align="center">
  <img src="https://raw.githubusercontent.com/DmitryUlyanov/dmitryulyanov.github.io/master/assets/typed_print/tp_logo.png">
</p>

Usually while I am fast developing on jupiter-notebook in 
training loops or functions I type something like this
`print("train.shape", train.shape)` or `print("Val metric is", val_metric)`
to monitor what is going on inside, and often it looks a bit wordy, and it is easy to get lost whe you 
are checking several variables like this `print(var1, var2, var3, var4)` as they are not tagged in the output.

So having free evening I decides to create this little tool to avoid such problems and improve my coding speed.

Many thanks to Dmitry Ulyanov and his typed_print for coloring inspiration.
 