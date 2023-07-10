import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  const pro = Promise.all([uploadPhoto(), createUser()]).then((values) => { console.log(`${values[0].body} ${values[1].firstName} ${values[1].lastName}`); })
    .catch(() => {
      console.log('Signup system offline');
    });
  return pro;
}
export default handleProfileSignup;
