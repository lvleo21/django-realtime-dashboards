const socket = new WebSocket('ws://' + window.location.host + '/ws/teste/')

socket.onmessage = (e) => {
    console.log("Server: ", e.data);
};

socket.onopen = (e) => {
    socket.send(JSON.stringify({
        'message': "Hello, server.",
        'sender': "Leonardo"
    }))
}