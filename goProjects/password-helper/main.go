package main
import "fmt"
func main(){
	var user_pw string
	fmt.Println("create a password, I will test how strong is it!")
	fmt.Scanln(&user_pw)
	pw_len:=len(user_pw)
	fmt.Println("You entered : ",user_pw)
	fmt.Println("You entered : ",pw_len)
	if pw_len < 8{
		fmt.Println("Your password is WEAK!")
		fmt.Println("Reason: Contains less than 8 characters: ",pw_len)
	}else if pw_len >=8 && pw_len<12{
		fmt.Println("Your password is MODERATE!")
                fmt.Println("Reason: Contains ",pw_len," characters")
	}else {
                fmt.Println("Your password is STRONG!")
                fmt.Println("Reason: Contains ",pw_len," characters")


	}

}
