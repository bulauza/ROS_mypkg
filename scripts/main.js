var ros = new ROSLIB.Ros({ url : 'ws://' + location.hostname + ':9000' });
                                                   
ros.on('connection', function() {console.log('websocket: connected');});
ros.on('error', function(error) {console.log('websocket error: ', error); });
ros.on('close', function() {console.log('websocket: closed');});

var ls1 = new ROSLIB.Topic({
        ros : ros,
        name : '/time_str',
        messageType : 'std_msgs/String'
});

var ls2 = new ROSLIB.Topic({
        ros : ros,
        name : '/status_led',
        messageType : 'std_msgs/String'
});

ls1.subscribe(function(message) {
        //str = JSON.stringify(message);
        //pstr = JSON.parse(str);
        //document.getElementById("count").innerHTML = pstr["data"];
        //console.log(pstr["data"]);                                  
        document.getElementById("date_time").innerHTML = message.data;
        console.log(message.data);                                  
});

ls2.subscribe(function(message) {
        document.getElementById("status_led").innerHTML = message.data;
        console.log(message.data);                                  
});
