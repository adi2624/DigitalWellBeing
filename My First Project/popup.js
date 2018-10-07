 let changeColor = document.getElementById('changeColor');

  chrome.storage.sync.get('color', function(data) {
    changeColor.style.backgroundColor = '#e8453c';
    changeColor.setAttribute('value', data.color);
    changeColor.onclick = function(element) {
        let color = element.target.value;
        
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.getSelected(null, function(tab) {
                myFunction(tab.url);
            });
          chrome.tabs.executeScript(
           
              tabs[0].id,
              {code: 'document.body.style.backgroundColor = "' + color + '";'});
        });
    };

   
    
    function myFunction(tablink) {
       // confirm('Your web url is \n'+tablink);
        const Url1 = 'http://35.237.208.254:5000/sendme';
        function_send(tablink,Url1);
      //  confirm('Your web url is after sending done \n'+tablink);
        console.log(tablink);  
    }

    function function_send(tablink,Url1)
    {
        var json;
        var obj_to_send = String(tablink);
        var data = {'name': obj_to_send, 'id':'stuff'};
        var xhr = new XMLHttpRequest();
        xhr.open("POST",Url1,true);
        xhr.setRequestHeader("Content-type","text/plain");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                json = JSON.parse(xhr.responseText);
   //             confirm("Recieved link is "+ json);
                console.log(json);
                send_to_devi(xhr.responseText,tablink);
            }
        };
        xhr.send(obj_to_send);

        
    }

    function send_to_devi(json,tablink)
    {
        var json2 ;
        const Url2 = 'http://35.229.124.91:5000/analyze';
        var xhr2 = new XMLHttpRequest();
        xhr2.open("POST",Url2,true);
        xhr2.setRequestHeader("Content-type","application/json");
        xhr2.send(json);
        xhr2.onreadystatechange = function () {
            if (xhr2.readyState === 4 && xhr2.status === 200) {
                json2 = xhr2.responseText;
                var jason3 =  JSON.parse(json);
                confirm("The Link: \n"+tablink+"\nWith Article: \n"+jason3.heading+"\nNEWS ANALYST SUGGEST THAT: "+json2);
                console.log(json2);
            }
        };
        
    }
  });