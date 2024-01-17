introducing the psuedo-language pyil!(pyil is pronouced "pile", the name is a combination of "py" and "IL"(since it was inspired by it))
<!--(specifically it's inspired by IL, [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck))-->
<!--MAKE IL THE ACTUAL LINK TO THE WIKIPEDIA PAGE-->

this language centers around incrementing, decrementing, etc a "pointer"(a number)

(for more context, look at the file while you read the printed out comments)

all whitespace execept spaces(unless it's not a valid action) is ignored

anything that is not a valid action is read as a comment(and therefore, is printed)

``


the most basic action is `print`, it prints out the pointer's current value

`print`

to stop a line from running completely, add `##` to the subtract

`##print`


the actions `add` and `sub` are the second most basic actions
they add X to the pointer and subtract X to and from the the pointer, respectively
added in v1.5: instead of a number, you can add `get` as the input and it will ask for an input then add/subtract from the pointer by that input
```
add 5
print
sub 1
print
```

the third most actions are `mul` and `div`
they multiply and divide the pointer by X, respectively

added in v1.5: instead of a number, you can add `get` as the input and it will ask for an input then multiply/divide the pointer by that input
```
mul 3
print
div 2
print
```


the `zero` action simply sets the pointer zero

`zero`




speaking of 'set', the `make` action sets the pointer to the given number

`make 15`




also speaking of 'set', the `get` action sets the pointer to the user's input

`get`




the `loop` action is interesting(it was also a little annoying to code, but uh...)
it goes in the format of `loop [times] [action] [action input]`
```
loop 2 add 3
print
```


the `is` action checks if the pointer is the given number, prints the result, and feeds it to the next `if` action

`is 10`


the `if/else/end` actions(in addition to being really annoying to code in) are a bit more complex than the previous
the `if` action is used as `if [True/False]`(it's not case-depentant, that's just a python habit)
if it is True/False, it will run the actions under it until the `else` action
the `else` action will run anything under it until the `end` action if it was not True/False
the `end` action is the end of each `if/else/end`; IT IS NEEDED, ALWAYS ADD IT
(comments can also be used optionally in a `if/else/end` like any other action)
**AS OF v1.5, THIS ACTION DOES NOT WORK**
```
if True
make 10
else
add 2
end
print
```


**added in v1.5:** the `goto` action let's you jump to any line before or ahead once(the index used starts at 0)
after v1.5.1: you can also add `rep` as a second input to make the `goto` repeat infinitely(use carefully)

`goto 68`

**added in v1.5:** the `lines` action shows the total lines of the file, including whitespace
`lines`

**added in v1.6:** the `wait` action can be used to wait for the user to press enter to continue
```
this is a comment
wait
this is a comment that happens after the wait
```

**added in v1.7:** the `totrans`, `trans`, and `cleartrans` actions are an interesting addition that allow for translation of the pointer to letter(the last index is a space, btw) or symbols
```
make 7
totrans
make 4
totrans
make 11
totrans
totrans
make 14
totrans

make -1
totrans

make 12
totrans
make 14
totrans
make 17
totrans
make 11
totrans
make 3
totrans

trans L
cleartrans
```
(this is a super crude implentation of these actions, btw)

and that's all pyil has to offer at this point!