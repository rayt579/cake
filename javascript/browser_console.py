'''
If we execute this in JS, what will the console show?


var text = 'outside';
function logIt(){
    console.log(text);
    var text = 'inside';
};
logIt();


The console will log undefined. 

The declaration gets hoisted to the top of the current scope


var text = 'outside';
function logIt(){
    var text;
    console.log(text);
    text = 'inside';
};
logIt();


Using "var" makes the declaration hoisted to the top of the current scope
Takeaways:
	1. Watch out for hoisting in JavaScript.
'''
