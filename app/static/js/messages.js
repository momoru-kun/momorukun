namespace = '/momoru.messages';
var socket = io(namespace);

socket.on('connect', function() {
    socket.emit('my_event', {data: 'I\'m connected!'});
});

socket.on('my_response', function(msg, cb) {
    if (msg.event == "message") {
        $('#messageSection').append("<br> <div class='message'><span>" + msg.name + ":&nbsp;</span>"+msg.data+"</div>");
        var scrl = $(".message")[$(".message").length - 1].offsetTop + $(".message")[$(".message").length - 1].offsetHeight;
        $("#messageSection").animate({scrollTop: scrl}, 0)
    } 
    else if (msg.event == "connect") {
        $("#Online").html(msg.online + " Online");
        console.log(msg);
    }
    else if (msg.event == "disconnect") {
        $("#Online").html(msg.online + " Online");
        console.log(msg);
    }
});


$(document).ready(function() {
    $('#send_message').click(function(event) {
        event.preventDefault();
        socket.emit('new_message', {data: {text: $('#message_text').val(), name: $('#message_name').val()}});
        $("#message_text").val("");
        return false;
    });
    $("#message_name").keyup(function(event){
        if(event.keyCode == 13){
            event.preventDefault();
        }
    });
    $("#message_text").keyup(function(event){
        if(event.keyCode == 13){
            event.preventDefault();
            socket.emit('new_message', {data: {text: $('#message_text').val(), name: $('#message_name').val()}});
            $("#message_text").val("");
            return false;
        }
    });
});