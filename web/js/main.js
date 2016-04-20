$("#submitButton").submit(function(){

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
    url:'data.php',
    type:'POST',
    data:s,
    success:function(data){
    $(".privacy_info").html(data);
    }
    error: function(xhr, desc, err) {
    console.log(xhr);
    console.log("Details: " + desc + "\nError:" + err);
    }
  }); // end ajax
});



$(function(){
  $('#submitButton').on('click', function(e){
    e.preventDefault();
    $('#followbtn').fadeOut(300);

    $.ajax({
      url: 'data.php',
      type: 'post',
      data: {'action': 'follow', 'userid': '11239528343'},
      success: function(data, status) {
        if(data == "ok") {
          $('#followbtncontainer').html('<p><em>Following!</em></p>');
          var numfollowers = parseInt($('#followercnt').html()) + 1;
          $('#followercnt').html(numfollowers);
        }
      },
      error: function(xhr, desc, err) {
        console.log(xhr);
        console.log("Details: " + desc + "\nError:" + err);
      }
    }); // end ajax call
  });
