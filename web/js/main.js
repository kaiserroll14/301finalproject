$(function(){
    $('#submitButton').on('click', function(e){
        e.preventDefault();

        var shape = $(".shape:checked").val();
        var color = $(".color:checked").val();
        var size  = $(".size:checked").val();
        var pos   = $(".pos:checked").val();

        var s = {
            "shape":shape,
            "color":color,
            "size":size,
            "pos":pos
        }

        $.ajax({
            url:'process.php',
            type:'POST',
            data:s,
            success:function(data){
                $("#banner").html(data);
            }
        }); // end ajax
    });
});
