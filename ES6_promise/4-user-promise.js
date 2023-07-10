function signUpUser(firstName, lastName) {
  const pro = Promise.resolve({
    firstName,
    lastName,
  })
  return pro
}
export default signUpUser;
