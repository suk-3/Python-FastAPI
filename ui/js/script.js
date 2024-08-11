const route_call = () => {
    $("#loading-screen").removeClass('hidden');

    data = new FormData()
    content = ""
    data.append('content', content)

    fetch('/routename', {
        method: 'POST',
        body: data
    }).then(function (response) {
        return response.json()
    }).then(function (resp) {
        data = resp?.data || []

        /* Logic to handle the data */

        $("#loading-screen").addClass('hidden');
    }).catch(function (error) {
        console.log("Error getting document:", error);
        $("#loading-screen").addClass('hidden');
    });
}