// The App Store listing (DECISIONS.md #114, #116): everything public is in store.config.json, tracked and linted
// by `./test.sh` (`listing`). Apple also requires a review contact's e-mail and phone, which stay out of the
// tree (the security gate refuses e-mail-shaped strings) and come from the environment of the one command
// that pushes: `./run.sh metadata push`, which refuses to run without them.
const base = require('./store.config.json');

const required = (name) => {
  const value = process.env[name];
  if (!value) throw new Error(`${name} is not set; see ./run.sh metadata push`);
  return value;
};

module.exports = {
  ...base,
  apple: {
    ...base.apple,
    review: {
      ...base.apple.review,
      email: required('EAS_REVIEW_EMAIL'),
      phone: required('EAS_REVIEW_PHONE'),
    },
  },
};
