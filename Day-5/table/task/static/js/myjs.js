
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
