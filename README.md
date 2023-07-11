# django_tdd_docker


This project is a part of the course: https://testdriven.io/courses/tdd-django/. 

- Django app with several endpoints and tests. 
- docker compose starts two containers. First one with my Django app. Second with Postres. 
- Project was deployed to Heroku (link does not work now): https://whispering-fortress-58832.herokuapp.com/api/movies/, https://whispering-fortress-58832.herokuapp.com/api/movies/2/, ... 
- to test endpoints in Heroku use http: 
- http GET https://whispering-fortress-58832.herokuapp.com/api/movies/
- http GET https://whispering-fortress-58832.herokuapp.com/api/movies/1/
- http --json POST https://whispering-fortress-58832.herokuapp.com/api/movies/ title=Fargo genre=comedy year=1996
- http --json PUT https://whispering-fortress-58832.herokuapp.com/api/movies/5/ title=Fargo genre=thriller year=1996
- http DELETE https://whispering-fortress-58832.herokuapp.com/api/movies/5/
- CI with two stages was added: build and tests. First stages passes second one fails. All tests passes locally. I'm not going to solve this issue.
