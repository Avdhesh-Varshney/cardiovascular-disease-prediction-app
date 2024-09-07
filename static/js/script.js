// Create form elements
const form = document.getElementById('predictionForm');

// Function to create a form element dynamically
function createFormElement(labelText, elementType, elementId, options) {
  const formGroup = document.createElement('div');
  formGroup.classList.add('mb-3');

  const label = document.createElement('label');
  label.setAttribute('for', elementId);
  label.classList.add('form-label');
  label.textContent = labelText;

  const formElement = document.createElement(elementType);
  formElement.classList.add('form-control');
  formElement.setAttribute('id', elementId);
  formElement.setAttribute('name', elementId);

  const placeholderOption = document.createElement('option');
  placeholderOption.setAttribute('value', '');
  placeholderOption.textContent = 'Select One';
  formElement.appendChild(placeholderOption);

  if (options) {
    options.forEach(option => {
      const optionElement = document.createElement('option');
      optionElement.setAttribute('value', option.value);
      optionElement.textContent = option.label;
      formElement.appendChild(optionElement);
    });
  }

  formGroup.appendChild(label);
  formGroup.appendChild(formElement);

  return formGroup;
}

// Function to create radio buttons dynamically
function createRadioButtons(labelText, elementId, values, text1, text2) {
  const formGroup = document.createElement('div');
  formGroup.classList.add('mb-3');

  const label = document.createElement('label');
  label.classList.add('form-label');
  label.textContent = labelText;
  formGroup.appendChild(label);

  values.forEach(value => {
    const radioDiv = document.createElement('div');
    radioDiv.classList.add('form-check', 'form-check-inline');

    const radioInput = document.createElement('input');
    radioInput.setAttribute('type', 'radio');
    radioInput.setAttribute('id', `${elementId}_${value}`);
    radioInput.setAttribute('name', elementId);
    radioInput.setAttribute('value', value);
    radioInput.classList.add('form-check-input');

    if (value === 0) {
      radioInput.setAttribute('checked', 'checked');
    }

    const radioLabel = document.createElement('label');
    radioLabel.setAttribute('for', `${elementId}_${value}`);
    radioLabel.textContent = value === 1 ? text1 : text2;
    radioLabel.classList.add('form-check-label');

    radioDiv.appendChild(radioInput);
    radioDiv.appendChild(radioLabel);
    formGroup.appendChild(radioDiv);
  });

  return formGroup;
}

// Function to create form input element dynamically
function createFormInput(labelText, elementId, placeholderText) {
  const formGroup = document.createElement('div');
  formGroup.classList.add('mb-3');

  const label = document.createElement('label');
  label.setAttribute('for', elementId);
  label.classList.add('form-label');
  label.textContent = labelText;

  const inputElement = document.createElement('input');
  inputElement.setAttribute('type', 'text');
  inputElement.classList.add('form-control');
  inputElement.setAttribute('id', elementId);
  inputElement.setAttribute('name', elementId);
  inputElement.setAttribute('required', true);
  inputElement.setAttribute('placeholder', placeholderText);

  formGroup.appendChild(label);
  formGroup.appendChild(inputElement);

  return formGroup;
}

// Function to create slider element dynamically
function createSlider(labelText, elementId, type, minValue, maxValue) {
  const formGroup = document.createElement('div');
  formGroup.classList.add('mb-3');

  const label = document.createElement('label');
  label.setAttribute('for', elementId);
  label.classList.add('form-label');
  label.textContent = labelText;

  const sliderGroup = document.createElement('div');
  sliderGroup.classList.add('slider-group');

  const sliderElement = document.createElement('input');
  sliderElement.setAttribute('type', 'range');
  sliderElement.setAttribute('id', elementId);
  sliderElement.setAttribute('name', elementId);
  sliderElement.setAttribute('min', minValue);
  sliderElement.setAttribute('max', maxValue);
  if (type === 'int') {
    sliderElement.setAttribute('step', '1');
  } else {
    sliderElement.setAttribute('step', '0.1');
  }
  sliderElement.setAttribute('value', minValue);
  sliderElement.classList.add('form-range');

  const valueDisplay = document.createElement('span');
  valueDisplay.classList.add('slider-value');
  valueDisplay.textContent = sliderElement.value;

  sliderElement.addEventListener('input', () => {
    valueDisplay.textContent = sliderElement.value;
  });

  sliderGroup.appendChild(sliderElement);
  sliderGroup.appendChild(valueDisplay);

  formGroup.appendChild(label);
  formGroup.appendChild(sliderGroup);

  return formGroup;
}

// Function to create button dynamically
function createButton(labelText) {
  const formElement = document.createElement('button');
  formElement.classList.add('btn', 'btn-danger');
  formElement.textContent = labelText;
  formElement.addEventListener('click', function (event) {
    if (!isFormValid()) {
      event.preventDefault();
      alert('Please fill the form carefully!');
    }
  });
  return formElement;
}

// Function to check if the form is valid (at least one option selected)
function isFormValid() {
  const selectElements = form.querySelectorAll('select');
  let count = 0;
  for (const selectElement of selectElements) {
    if (selectElement.value !== '') {
      count++;
    }
  }
  const heightInput = form.querySelector('#height');
  const weightInput = form.querySelector('#weight');
  const numericRegex = /^(\d+(\.\d+)?)?$/;
  if (!numericRegex.test(heightInput.value) || !numericRegex.test(weightInput.value)) {
    return false;
  }
  return count === selectElements.length;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

form.appendChild(createFormInput('Enter your name:', 'name', ""));

form.appendChild(createFormElement('In what age category do you belong?', 'select', 'age_category', [
  { value: 0, label: '18-24' },
  { value: 1, label: '25-29' },
  { value: 2, label: '30-34' },
  { value: 3, label: '35-39' },
  { value: 4, label: '40-44' },
  { value: 5, label: '45-49' },
  { value: 6, label: '50-54' },
  { value: 7, label: '55-59' },
  { value: 8, label: '60-64' },
  { value: 9, label: '65-69' },
  { value: 10, label: '70-74' },
  { value: 11, label: '75-79' },
  { value: 12, label: '80+' },
]));

form.appendChild(createRadioButtons('Sex', 'sex', [1, 0], 'Male', 'Female'));
form.appendChild(createFormInput('Height (in cm)', 'height', ''));
form.appendChild(createFormInput('Weight (in kg)', 'weight', ''));
form.appendChild(createRadioButtons('Have you smoked at least 100 cigarettes in your entire life?', 'smoking_history', [1, 0], 'Yes', 'No'));

form.appendChild(createFormElement('General Health', 'select', 'general_health', [
  { value: 3, label: 'Poor' },
  { value: 1, label: 'Fair' },
  { value: 2, label: 'Good' },
  { value: 4, label: 'Very Good' },
  { value: 0, label: 'Excellent' },
]));

form.appendChild(createFormElement('Checkup', 'select', 'checkup', [
  { value: 1, label: 'Never' },
  { value: 4, label: 'Within the past year' },
  { value: 2, label: 'Within the past 2 years' },
  { value: 3, label: 'Within the past 5 years' },
  { value: 0, label: '5 or more years ago' },
]));

form.appendChild(createFormElement('Diabetes', 'select', 'diabetes', [
  { value: 0, label: 'No' },
  { value: 1, label: 'No, pre-diabetes or borderline diabetes' },
  { value: 2, label: 'Yes' },
  { value: 3, label: 'Yes, but female told only during pregnancy' },
]));

form.appendChild(createRadioButtons('During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?', 'exercise', [1, 0], 'Yes', 'No'));
form.appendChild(createRadioButtons('Skin Cancer', 'skin_cancer', [1, 0], 'Yes', 'No'));
form.appendChild(createRadioButtons('Other Cancer', 'other_cancer', [1, 0], 'Yes', 'No'));
form.appendChild(createRadioButtons('Depression', 'depression', [1, 0], 'Yes', 'No'));
form.appendChild(createRadioButtons('Arthritis', 'arthritis', [1, 0], 'Yes', 'No'));
form.appendChild(createSlider('During the past 30 days, how many days did you have at least one drink of any alcoholic beverage such as beer, wine, a malt beverage or liquor?', 'alcohol_consumption', 'float', 0, 30));
form.appendChild(createSlider('Not including juices, how often did you eat fruit?', 'fruit_consumption', 'float', 0, 120));
form.appendChild(createSlider('How often did you eat a green leafy or lettuce salad, with or without other vegetables?', 'green_vegetables_consumption', 'float', 0, 128));
form.appendChild(createSlider('How often did you eat any kind of fried potatoes, including French fries, home fries, or hash browns?', 'fried_potato_consumption', 'float', 0, 128));

form.appendChild(createButton('Predict'));
