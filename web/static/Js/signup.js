	var f;
	var mycaptch;
function mycap()
{
var a = Math.random()+1;
var d = a*6;
	if(d>=10)
	{
		f="A";
	}
	else if(d>=7)
	{
		f="B";
	}
	else if(d>=4)
	{
		f="C";
	}
	else
	{
		f="D";
	}
var b = parseInt(a*12);
var x = parseInt(a*146);
 mycaptch = b+f+x;
document.getElementById('code').innerHTML=mycaptch;
console.log(d);
}

//setInterval("mycap()",000);
window.onload=function()
{
	mycap();
}
window.onchange=function()
{
    validate_captcha();
}


function validate_captcha()
{
    var a,final;
    a=document.getElementById('captcha');
    final=a.value;
    if (final!==mycaptch)
    {
    msg="Invalid captcha";
    document.getElementById('error').innerHTML=msg;

    }
}