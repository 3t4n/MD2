/*dash board*/

var app = angular.module("MD2", ['ngRoute', 'ngCookies']);

function isEmpty(ob){ for(var i in ob){ return false;}return true;};

app.config(function ($httpProvider) {
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
});


app.controller('generarMundoController',
               function generarMundoController($scope,$http,$sce)
               {
                   $scope.x="";
                   $scope.y="";
                   $scope.lados = "";
                   $scope.porcentaje = "";
                   $scope.enunciados = "";
                   $scope.subenunciados = "";
                   $scope.res = null;
                   $scope.correcto = [];
                   $scope.matrix = [];
                   $scope.vacio = function (obj) {  if(Object.keys(obj).length == 1) return true; return false;};
                   
                   $scope.coord = function (ob,size) {
                       var temp = "";
                       for(var i=0; i<ob.length;i++)
                       {
                           var x = ob[i]["x"]*size/2 + size/2;
                           var y = ob[i]["y"]*size/2 + size/2;
                           temp = temp + x +"," + y +" ";
                       }
                       /*console.log(temp);*/
                       return  temp;
                   };

                   $scope.generarMundo = function()
                   {
                       $scope.correcto = [];
                       $http({
                           method: 'POST',
                           url: '/generarMundo',
                           data: "x="+$scope.x+"&y="+$scope.y+"&lados="+$scope.lados+"&porcentaje="+$scope.porcentaje+"&subenunciados="+$scope.subenunciados + "&enunciados=" + $scope.enunciados,
                       }).then(function(response){
                           $scope.res = response.data;
                       });
                   };
                   $scope.checar = function(id,valor)
                   {
                               if($scope.res["preguntas"][id]["res"]==valor)
                               {
                                    $scope.correcto[id]="Correcto";

                               }
                               else
                               {
                                    $scope.correcto[id]="Incorrecto";
                                   
                               }
                   }
               }

);

app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "../static/templates/generarMundoController.html",
    });
});
