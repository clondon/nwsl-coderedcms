$('#watfordwills_header_banner').css({'height': (($(window).height()))+'px'});
$(window).on('resize', function(){
    $('#watfordwills_header_banner').css({'height': (($(window).height()))+'px'}).css({'background-position': 'top'});
   });