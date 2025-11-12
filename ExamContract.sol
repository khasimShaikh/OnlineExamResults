pragma solidity >= 0.8.11 <= 0.8.11;
pragma experimental ABIEncoderV2;
//cheque solidity code
contract ExamContract {

    uint public studentCount = 0; 
    mapping(uint => student) public studentList; 
     struct student
     {
       string studentId;
       string name;
       string firstQuestion;
       string secondQuestion;
       string thirdQuestion;
       string fourthQuestion;
       string fifthQuestion;
       string completeDate; 
       string timeTaken;
       string grade;
     }
 
   // events 
   event studentCreated(uint indexed _studentId);

  
   //function  to save grade details
   function createGrade(string memory sid, string memory sname, string memory first, string memory second, string memory third, string memory fourth, string memory fifth, string memory cd, string memory tt, string memory g) public {
      studentList[studentCount] = student(sid, sname, first, second, third, fourth, fifth, cd, tt, g);
      emit studentCreated(studentCount);
     studentCount++;
    }

     //get student count
    function getStudentCount()  public view returns (uint) {
          return  studentCount;
    }

    function getStudentId(uint i) public view returns (string memory) {
        student memory s = studentList[i];
	return s.studentId;
    }

    function getName(uint i) public view returns (string memory) {
        student memory s = studentList[i];
	return s.name;
    }

    function getFirstQuestion(uint i) public view returns (string memory) {
        student memory s = studentList[i];
	return s.firstQuestion;
    }

    function getSecondQuestion(uint i) public view returns (string memory) {
        student memory s = studentList[i];
	return s.secondQuestion;
    }

    function getThirdQuestion(uint i) public view returns (string memory) {
        student memory s = studentList[i];
	return s.thirdQuestion;
    }
    function getFourthQuestion(uint i) public view returns (string memory) {
        student memory s = studentList[i];
	return s.fourthQuestion;
    }
    function getFifthQuestion(uint i) public view returns (string memory) {
        student memory s = studentList[i];
	return s.fifthQuestion;
    }

    function getDate(uint i) public view returns (string memory) {
        student memory s = studentList[i];
	return s.completeDate;
    }

    function getTime(uint i) public view returns (string memory) {
       student memory s = studentList[i];
	return s.timeTaken;
    }

    function getGrade(uint i) public view returns (string memory) {
        student memory s = studentList[i];
	return s.grade;
    }

    uint public userCount = 0; 
    mapping(uint => user) public usersList; 
     struct user
     {
       string username;
       string password;     
       
     }
 
   // events
 
   event userCreated(uint indexed _userId);
 
  function createUser(string memory _username, string memory _password) public {
      usersList[userCount] = user(_username, _password);
      emit userCreated(userCount);
      userCount++;
    }

    
     //get user count
    function getUserCount()  public view returns (uint) {
          return  userCount;
    }

    function getUsername(uint i) public view returns (string memory) {
        user memory usr = usersList[i];
	return usr.username;
    }

    function getPassword(uint i) public view returns (string memory) {
        user memory usr = usersList[i];
	return usr.password;
    }    
    
}