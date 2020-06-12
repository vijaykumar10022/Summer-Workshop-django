
// alert(" hello Django");
	// document.getElementById("mysc").innerHTML ="Hello Django";

// var person = new Object();
// person.firstName = "John";
// person.lastName = "Doe";
// person.age = 50;
// person.eyeColor = "blue"; 

// document.getElementById("mysc").innerHTML = person.firstName + " is " + person.age + " years old.";
var temp1=0
function team1() {
			var First_num=document.getElementById('fn1').value;// 2 ,6
			document.getElementById('result1').innerText=parseInt(First_num)+temp1;//2,6+2
			temp1=temp1+parseInt(First_num);// 0+2-->2,2+6-->8
			// body...
	}
var temp2=0
function team2() {
			var First_num=document.getElementById('fn2').value;
			document.getElementById('result2').innerText=parseInt(First_num)+temp2;
			temp2=temp2+parseInt(First_num)
			// body...
	}

function result(){
	// document.getElementById('result').innerText=temp1+temp2;
	if (temp1>temp2){
		document.getElementById('won').innerText="Team1 Won the Match "+temp1;
	}
	else{
		document.getElementById('won').innerText="Team2 Won the Match"+temp2;
	}
	
	
}

function strongpassword(){
	var firstName=document.getElementById('fname').value;
	data=firstName.slice(0,2);
	var lastName=document.getElementById('lname').value;
	data=data+"!"+lastName.slice(0,2);
	var phno=document.getElementById('phno').value;
	data=data+"@"+phno.slice(phno.length-2,phno.length);
	document.getElementById('result').innerText="Your Strong Password is :"+data;

}

function checkpassword(){
	var Password=document.getElementById('password').value;
	var i=0
	for (i=0;i<=Password.length;i++){
		if(Password[i]>='a' && Password[i]<='z' || Password[i]>='A' && Password[i]<='Z'){
			document.getElementById('result').innerText="Week Password";

		}
		else if(Password[i]>='a' && Password[i]<='z' && Password[i]>='A' && Password[i]<='Z' && Password[i]>='0' and Password[i]<='9'){
			document.getElementById('result').innerText="Good Password";
		}
		else {
			document.getElementById('result').innerText="very strong Password";

		}
	}
}