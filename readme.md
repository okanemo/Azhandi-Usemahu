<h1>README</h1>
<hr>
<h3>Requirements<li>
  <ul>
    <li>already installed Docker</li>
    <li>Already installed Postman</li>
    <li>pgadmin</li>
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
 <hr>
 <ol>
    <li>open pgadmin</li>
    <li>create new server</li>
    <li>on the connection tab, input :
      <ul>
        <li>host : localhost</li>
        <li>port : 5000</li>
        <li>username : postgres</li>
        <li>password : postgres</li>
      </ul>
      <li>save the configuration</li>
 </ol>
  
  <h3>Run the application<h3>
  <hr>
   <ol>
    <li>make sure the app is running (with run-command on the app directory: docker-compose up)</li>
    <li>on postman, set the URL to localhost:8000 and method to POST</li>
    <li>on the body, set to raw-JSON and input the JSON data</li>
    <li>click send on the url field</li>
 </ol>
  
<p> if success it will return <br>
  {'Success': 'Patient data added'} <br>
    if fail it will return a json with what the error is
</p>


  
