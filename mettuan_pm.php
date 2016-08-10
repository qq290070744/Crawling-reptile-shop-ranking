<!DOCTYPE html>
<html>
<head>
<?php
include "config.php";
session_start();
if(!isset($_SESSION['username'])){
    $home_url = 'logIn.php';
header('Location:'.$home_url);
    }
$ms=0;
$mt=0;
$ds=0;
$dt=0;
     
?>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>主页</title>
 
<script src="js/jquery-1.9.1.min.js" type="text/javascript"></script>
<script src="js/bootstrap-select.js" type="text/javascript"></script>
<script type="text/javascript" src="grid.js"></script>
    <link id="bs-css" href="css/bootstrap-cerulean.min.css" rel="stylesheet">
    <link href="css/charisma-app.css" rel="stylesheet">      
    <link href="css/bootstrap-select.css" rel="stylesheet">
    <link href='bower_components/fullcalendar/dist/fullcalendar.css' rel='stylesheet'>
    <link href='bower_components/fullcalendar/dist/fullcalendar.print.css' rel='stylesheet' media='print'>
    <link href='bower_components/chosen/chosen.min.css' rel='stylesheet'>
    <link href='bower_components/colorbox/example3/colorbox.css' rel='stylesheet'>
    <link href='bower_components/responsive-tables/responsive-tables.css' rel='stylesheet'>
 
    <link href='bower_components/bootstrap-tour/build/css/bootstrap-tour.min.css' rel='stylesheet'>
    <link href='css/jquery.noty.css' rel='stylesheet'>
    <link href='css/noty_theme_default.css' rel='stylesheet'>
    <link href='css/elfinder.min.css' rel='stylesheet'>
    <link href='css/elfinder.theme.css' rel='stylesheet'>
    <link href='css/jquery.iphone.toggle.css' rel='stylesheet'>
    <link href='css/uploadify.css' rel='stylesheet'>
    <link href='css/animate.min.css' rel='stylesheet'>
 
 
<link href="grid.css" type="text/css" rel="stylesheet"> 
<script type="text/javascript" src="laydate/laydate.js"></script>
<script type="text/javascript" src="bower_components/responsive-tables/responsive-tables.js"></script>
<script type="text/javascript"> laydate.skin('danlan');</script>
<script src="js/jquery.noty.js"></script>
 
 
 
 
 
</head>
<body>
    <!-- topbar starts -->
    <?php include 'dropdownmenu.php' ?>
    <!-- topbar ends -->
<div class="ch-container" style="position:relative;top:80px">
    <div class="row">
     
     
     
<?php include 'navi.php'; ?>
         
         
         
        <div id="content" class="col-lg-10 col-sm-10">
            <!-- content starts -->
        <div id="dlayerreport">
 
</div>    
         
<div class="row">
    <div class="box col-md-12">
        <div class="box-inner">
            <div class="box-header well">
                <h2><i class="glyphicon glyphicon-info-sign"></i>美团店铺排名</h2>
                <div class="box-icon">
                    <a href="orderlist.php" class="btn btn-minimize btn-round btn-default"><i class="glyphicon glyphicon-chevron-up"></i></a>
                </div>
            </div>
            <div class="box-content row">
                <div class="col-lg-7 col-md-12" style="width:100%;">
 <div id="wepaydailysales" class="box-content" style="width:100%;">
   <form id="grid_form_id">
       <table class="table table-striped table-bordered bootstrap-datatable datatable responsive">    
            <thead><tr>
            <!--<th class="th1" style="width:5%;">排序</th>-->
            <th class="th1" style="width:15%;">店铺</th>
            <th class="th2"  style="width:15%;">排名</th>
            <th class="th5"  style="width:25%;">更新时间</th>
            <th class="th4"  style="width:25%;"> 定位地址</th>
             
             
            </tr></thead>
<?php            
 
      $serverName = "localhost"; 
        $connectionInfo = array(  "UID"=>"stdservice", "PWD"=>"数据库密码","Database"=>"STDdata"); 
        $conn = sqlsrv_connect( $serverName, $connectionInfo);
    $queryString = "SELECT * FROM dbo.meituan_paiming ORDER BY paiming aSC";
        if($result = sqlsrv_query($conn,$queryString))
    {
        $lb='';
        $num=0;
      while($row = sqlsrv_fetch_array( $result,SQLSRV_FETCH_ASSOC))
      {
        $num=$num+1;
        //$action='<a class="btn btn-info" style="margin-left:10px;" data-toggle="modal" href="#menu" onclick="show(\''.$row['goodsid'].'\',\''.iconv("gbk//ignore", "utf-8",$row['goodsname']).'\');"><i class="glyphicon glyphicon-zoom-in icon-white"></i>修改</a>';
        //$lb=iconv("gbk//ignore", "utf-8",$row['classid2']);
        //if( strpos($lb, '1') !== false){
        //$lb='超值';
        //}else if( strpos($lb, '2') !== false){
        //$lb='简餐';
        //}else if(strpos($lb, '3') !== false){
        //$lb='套餐';
        //}else if (strpos($lb, '4') !== false){
        //$lb='炖汤';
        //}else if (strpos($lb, '5') !== false){
        //$lb='小吃';
        //}else if (strpos($lb, '6') !== false){
        //$lb='积分换购';
        //}else{
        //$lb='未分类';
        //};
        //echo '<td>'.iconv("gbk//ignore", "utf-8",$num).'</td>';
        echo '<td>'.iconv("gbk//ignore", "utf-8",$row['store_name']).'</td>';
        //echo '<td>'.$row['store_name'].'</td>';
        echo '<td>'.$row['paiming'].'</td>';
         
        echo '<td>'.iconv("gbk//ignore", "utf-8",$row['updatetime']).'</td>';
        echo '<td>'.iconv("gbk//ignore", "utf-8",$row['dingwei_address']).'</td>';
        //echo '<td>'.$row['price'].'</td>';
      //  echo '<td>'.$lb.'</td>';
       // echo '<td>'.$row['classid'].'</td>';
        //echo '<td>'.$row['meituanID'].'</td>';  
       // echo '<td><img border="0" width="80px" src="getimage.php?id='.$row['goodsid'].'" ></td>';
        //echo '<td>'.$action.'</td>';
        echo '</tr>';
      }
 
    }
    sqlsrv_close($conn);
  
?>
 
<script language="javascript">
   function show(itemid,itemname) {
$("#itemid").attr("value",itemid);
$("#itemname").html(itemname);
    }
</script>
 
</table></form></div>
                </div>
            </div>
        </div>
    </div>
</div>
 
</div>
 
 
<div class="modal fade" id="menu" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true" style="display: none;">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">×</button>
                    <h3 id="itemname"></h3>
                </div>
                <div class="modal-body">
                    <form class="form-horizontal" action="action_updateimage.php" method="post"  enctype="multipart/form-data" >
                    <fieldset>
                    <div class="input-group input-group-lg">
                     
                    <div style="display:none;" class="col-sm-8"><input type="text" name="itemid" id="itemid" class="form-control" readonly ="readonly"></div>
                    </div>   
 
                    <div class="input-group input-group-lg">
                    <span class="input-group-addon"><i class="glyphicon glyphicon-folder-open red"></i></span>
                    <input type="file" name="FileUpload1" id="FileUpload1"  class="btn btn-primary green" />
                    </div>                   
                     
                     
                </div>
                 <div  class="clearfix"></div><br>
                         <p style="text-align:center"> <button type="submit" name="submit" class="btn btn-primary" style="text-align:center">确认</button></p>
                </form>
                <div class="modal-footer">
                    <a href="rider" class="btn btn-default" data-dismiss="modal">关闭</a>
                </div>
             </div>
         </div>
 </div>
 
 
 
<?php include 'userprof.php'; ?>
<?php include 'footer.php'; ?>
</div>
</body>
</html>
