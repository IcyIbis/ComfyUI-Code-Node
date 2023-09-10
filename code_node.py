# I definitely didn't steal this from logic nodes
class AlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False

class CodeNode:
	CATEGORY = "utils"
	
	@classmethod
	def INPUT_TYPES(s):
		return {
			"required": {
				"code_input": ("STRING", {"multiline": True,})
			},
			"optional": {
				"input_0": (AlwaysEqualProxy("*")),
				"input_1": (AlwaysEqualProxy("*")),
				"input_2": (AlwaysEqualProxy("*")),
				"input_3": (AlwaysEqualProxy("*")),
				"input_4": (AlwaysEqualProxy("*")),
				"input_5": (AlwaysEqualProxy("*")),
				"input_6": (AlwaysEqualProxy("*")),
				"input_7": (AlwaysEqualProxy("*")),
				"input_8": (AlwaysEqualProxy("*")),
				"input_9": (AlwaysEqualProxy("*")),
			},
		}
	
	RETURN_TYPES = (AlwaysEqualProxy("*"),AlwaysEqualProxy("*"),AlwaysEqualProxy("*"),AlwaysEqualProxy("*"),AlwaysEqualProxy("*"),AlwaysEqualProxy("*"),AlwaysEqualProxy("*"),AlwaysEqualProxy("*"),AlwaysEqualProxy("*"),AlwaysEqualProxy("*"))
	RETURN_NAMES = ("output_0","output_1","output_2","output_3","output_4","output_5","output_6","output_7","output_8","output_9")
	
	FUNCTION = "execute"
	
	# TODO: Could add in some special functions accessible to the `exec` to help users with debugging and stuff.
	# Maybe also make a token effort to sandbox... but then restricting what the code can do kinda goes against the point of having a node for any hacky purpose...
	def execute(self, code_input, input_0 = None, input_1 = None, input_2 = None, input_3 = None, input_4 = None, input_5 = None, input_6 = None, input_7 = None, input_8 = None, input_9 = None):
		inputs = (input_0, input_1, input_2, input_3, input_4, input_5, input_6, input_7, input_8, input_9)
		outputs = {
			0: None,
			1: None,
			2: None,
			3: None,
			4: None,
			5: None,
			6: None,
			7: None,
			8: None,
			9: None,
		} # a dictionary for the anarchists who don't want their outputs in a continuous order
		
		def do_input(inputs, outputs):
			exec(code_input)
		
		# This is where we'd put error handling, but I don't know how to do that
		do_input(inputs, outputs)
		
		return (outputs[0], outputs[1], outputs[2], outputs[3], outputs[4], outputs[5], outputs[6], outputs[7], outputs[8], outputs[9])

NODE_CLASS_MAPPINGS = {
    "CodeNode": CodeNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CodeNode": "Code Node ⚠"
}