# MyHDL2.0
MyHDL2.0 builds on MyHDL (see https://github.com/myhdl/myhdl and https://www.myhdl.org)

## Credits
We will for ever be indebted to [Jan Decaluwe](https://www.jandecaluwe.com), the original creator and BDFL of MyHDL  
His copyright will be maintained for all borrowed code.

## Observations on MyHDL
Except for the `Signal` and the *ingenious* `intbv()` objects original MyHDL uses native Pyton objects to represent RTL constructs.
- using `bool()` to represent the single bit  
- using *anonymous* classes to represent both `Structure` and `Interface` 
- using *anonymous* list to represent `Array`
These *anonymous* objects make life difficult as e.g. they lack assignment.
The conversion to both **VHDL** and **Verilog** is a single pass where the output is written *as fast as possible* 

## Goals and Targets
We will introduce new classes, `bit`, `Structure`, `Interface` and `Array`, to replace the native objects  
We will rework the conversion to a two-stage process where we first create an intermediate structure to represent the initial source code; the second pass will then convert the code to final **VHDL**, **Verilog**, **SystemVerilog** or **future other** reprersentation  
We intend to add hierchical conversion  
We will try to add a `Parameter` object to mimic **VHDL**'s `generic` construct

## Notes
First efforts will target simulution (first!) and conversion to **VHDL**; conversion to thers will then follow

