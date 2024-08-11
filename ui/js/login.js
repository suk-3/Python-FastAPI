var login = {
    reset: () => {
        $('#username').val('');
        $('#password').val('');
    },
    process: () => {
        var username = $('#username').val();
        var password = $('#password').val();

        if (username == '' || password == '') {
            $("#message").html('Please enter username and password');
            return;
        }

        $("#loading-screen").removeClass('hidden');

        data = new FormData()

        data.append('username', username)
        data.append('password', password)

        fetch('/login', {
            method: 'POST',
            body: data
        }).then(function (response) {
            return response.json()
        }).then(function (resp) {
            data = resp?.data || []

            data?.status = 'success' ? (window.location.href = '/dashboard') : $("#message").html('Invalid username or password');

            $("#loading-screen").addClass('hidden');
        }).catch(function (error) {
            console.log("Error getting document:", error);
            $("#loading-screen").addClass('hidden');
        });


\
    }
}