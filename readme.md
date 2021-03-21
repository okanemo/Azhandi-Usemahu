<h1>REAMDME</h1>
hr
<h3>Requirements<li>
  <ul>
    <li>already installed Docker</li>
    <li>Already installed Postman</li>
    <li>pgadmin<li>
  </ul>
<h3>How to use<h3>
<h4>Setting up the Application<h4>
<hr>
<ol>
  <li>run Docker Engin</li>
  <li>open command-promt in the app directory (../takeapi)</li>
  <li>run command : docker-compose up</li>
  <li>(optional) If the docker haven't up yet, terminate the proccess (ctrl+c) then run-command docker-compose up again</li>
  <li>open another command-pront on the app directory then run-command : docker exec -it takeapi_web_1 bash</li>
  <li>run-command : python manage.py migrate </li>
  <li>to be able to access Django Administation, can also run-command python manage.py createsuperuser</li>
  <li>terminate the proccess with ctrl+z</li>
</ol>
    
<h4>Setting up the database<h4>
 <ol>
    <li>open pgadmin<li>
    <li>create new server<li>
    <li>on the connection tab, input :
      <ul>
        <li>host : localhost<li>
        <li>port : 5000<li>
        <li>username : postgres<li>
        <li>password : postgres</li>
      </ul>
      <li>save the configuration<li>
    <li>
 </ol>


  
