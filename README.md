Code Nodes execute input python code, accepting inputs of any type, and give outputs of any type. They're intended to help with jury rigging workflows together, providing an option to perform custom code without having to create a dedicated node for it.

Since any python code can be run (without sandboxing), users should be cautious about using workflows containing Code Nodes they've acquired from outside sources (though I guess the same applies to mindlessly downloading nodes off the net, too :P).

## Usage
In `code_input`, enter the python code you want to execute. The values from the node's inputs can be accessed via `inputs[index]`, and output values can be assigned via `outputs[index]`.
### Code example
```py
# MULTI CONDITIONING APPLY
# Takes any number of conditionings and applies various outputs
# outputs[0] is all the conditionings combined
# output[1] is all the conditionings concatenated
# output[2] is all the conditionings averaged at a weight of 1
functions = dict() 

from nodes import ConditioningCombine, ConditioningConcat, ConditioningAverage

functions["combine"] = ConditioningCombine().combine
functions["concat"] = ConditioningConcat().concat
functions["average"] = ConditioningAverage().addWeighted

combined = inputs[0]
concatenated = inputs[0]
averaged = inputs[0]

next_index = 1

while True:
	if not inputs[next_index]:
		break
	
	new_conditioning = inputs[next_index]
	
	combined = functions["combine"](combined, new_conditioning)[0]
	concatenated = functions["concat"](concatenated, new_conditioning)[0]
	averaged = functions["average"](averaged, new_conditioning, 1.0)[0]
	
	next_index += 1

outputs[0] = combined
outputs[1] = concatenated
outputs[2] = averaged
```

## Wishlist
- Warn user the first time a workflow with a Code Node present would be run, highlighting the nodes and contents so they can check the included code.
- Maybe options for sandboxing, or at least a sandboxed alternative node(?)
- Dynamically adaptive input and output counts, so they can be of any length (is that possible?)

## Support and Issues
I have no intention of providing any further updates or support. Others are welcome to take over supporting this as they wish.
### Known Issues
- Curly braces within `code_input` will create syntax errors. To declare dictionaries, use `dict()` instead. (I don't know what causes this)

## Credits
Uses a snippet of code from [David Fischer's ComfyUI-Logic](https://github.com/theUpsider/ComfyUI-Logic)