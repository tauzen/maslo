function getCookie(name){
  if (document.cookie.length > 0) {
    begin = document.cookie.indexOf(name+"=");
    if (begin != -1) {
      begin += name.length+1;
      end = document.cookie.indexOf(";", begin);
      if (end == -1) end = document.cookie.length;
      return unescape(document.cookie.substring(begin, end));
    }
  }
  return null;
}

function setCookie(name, value, expiredays) {
  var expireDate = new Date ();
  expireDate.setTime(expireDate.getTime() + (expiredays * 24 * 3600 * 1000 * 5));

  document.cookie = name + "=" + escape(value) + ((expiredays === null) ? "" : "; expires=" + expireDate.toGMTString());
}

function acceptCookie() {
	setCookie('cookiepopup','yes',365);
	
	var link = document.getElementById('cookiepopup');
	link.style.display = 'none';
	link.style.visibility = 'hidden';
}

function cookiePopup() {
  cookie = getCookie('cookiepopup');
  if (cookie === null) {
    document.getElementById('cookiepopup').style.display = 'block';
    document.getElementById('cookiepopupbtn').onclick = acceptCookie;
  }
}

cookiePopup();