  Feature: SearchHotel
      Background: common steps
          Given Launch Chrome Browser
          When Open Webpage phptravels
          Then Verify Account visible
          Then Click Account
          When Enter username "jmarijanovic000@gmail.com" and password "123456789jm"

      Scenario: Login
          Then Profile Picture visible

      Scenario: SearchHotel
          When Navigate to Flights
          And Enter Flight "DUB" to "DXB"
          And Search Flights
          Then List of Flights is visible












