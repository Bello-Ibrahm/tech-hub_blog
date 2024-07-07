
$(function () {
    // CodeMirror
    CodeMirror.fromTextArea(document.getElementById("codeMirrorTextDesc"), {
        mode: "htmlmixed",
        lineNumbers: true,
        theme: "monokai"
    });
});

// Initialize CodeMirror
// var editor = CodeMirror.fromTextArea(document.getElementById("codeMirrorTextDesc"), {
//     mode: "htmlmixed",
//     lineNumbers: true,
//     theme: "default"
// });

$(function () {
    $("#example1").DataTable({
        "responsive": true, "lengthChange": false, "autoWidth": false,
        "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
    }).buttons().container().appendTo('#example1_wrapper .col-md-6:eq(0)');
});

$(function () {
    //Add text editor
    $('#post-textarea').summernote()
});
