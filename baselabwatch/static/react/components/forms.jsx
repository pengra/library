
class Form extends React.Component {
  // props:
    // url : url to OPTIONS/GET to find form contents
    // className : this html class
    // id : this html id
  constructor() {
    super();
    this.state = {
      formData: {},
      errors: {}
    };
  }

  // Overload methods:
  renderForm = () => {}
  onSubmitSuccess = (data) => {
    this.setState({
      success: true
    })
    setTimeout(() => {
      this.setState({
        success: false
      });
    }, 3000)
  }
  onSubmitFail = (data) => {
    this.setState({
      errors: data.responseJSON
    })
    this.setState({
      fail: true
    })
  }

  onChange = (event) => {
    this.updateFormDataState(event.target.name, "value", event.target.value);
  }
  handleSubmit = (event) => {
    event.preventDefault();
    $.ajax({
      method: this.state.method,
      url: this.props.url,
      data: this.serializeForm()
    })
    .done((data) => {
      this.onSubmitSuccess(data);
    })
    .fail((data) => {
      this.onSubmitFail(data);
    });
  }
  serializeForm = () => {
    let formContents = {};
    Object.keys(this.state.formData).map((k, i) => {
      formContents[k] = this.state.formData[k].value
    })
    return formContents;
  }
  updateFormDataState(field, key, value) {
    let newFormData = this.state.formData;
    let data = this.state.formData[field];
    data[key] = value;
    newFormData[field] = data;
    this.setState({
      formData: newFormData
    });
  }
  componentDidMount() {
    $.ajax({
      method: 'GET',
      url: this.props.url
    }).done((data) => this.loadForm(data, 'GET'));
    $.ajax({
      method: 'OPTIONS',
      url: this.props.url
    }).done((data) => this.loadForm(data, 'OPTIONS'));
  }
  loadForm = (data, verb) => {
    let newFormData = this.state.formData;
    if (verb === 'GET') {
      for (let fieldName in data) {
        if (fieldName in newFormData) {
          newFormData[fieldName].value = data[fieldName];
        } else {
          newFormData[fieldName] = {value: data[fieldName]};
        }
      }
    } else if (verb === 'OPTIONS' && data.actions) {
      let acceptedMethod = null;
      if ('PUT' in data.actions) {
        acceptedMethod = 'PUT';
      } else if ('POST' in data.actions) {
        acceptedMethod = 'POST';
      } else {
        throw "Unknown accepted method";
      }
      this.setState({method: acceptedMethod})
      const fields = data.actions[acceptedMethod]
      for (let fieldName in fields) {
        if (fieldName in newFormData) {
          newFormData[fieldName].options = fields[fieldName];
        } else {
          newFormData[fieldName] = {options: fields[fieldName]};
        }
      }
    }
    this.setState({formData: newFormData});
  }
  render() {
    let formRender = null;
    if (this.state.formData) {
      formRender = this.renderForm();
    }
    return (
      <form noValidate id={this.props.id} className={this.props.className || null} id={this.props.idName} onSubmit={this.handleSubmit}>
        {formRender}
      </form>
    )
  }
}

class SubmitInput extends React.Component {
  // props:
    // label: what to display on button
    // success : true/false success?
    // fail : true/false fail?
  render() {
    let feedback = null;
    if (this.props.success) {
      feedback = (
        <span className="ajax-notification text-success">
          <i className="fa fa-check" aria-hidden="true"></i> Updated
        </span>
      )
    } else if (this.props.fail) {
      feedback = (
        <span className="ajax-notification text-danger">
        <i className="fa fa-times" aria-hidden="true"></i> Failed. Try Again
      </span>
      )
    }
    return (
      <div>
      <input type="submit" value={this.props.label} className="btn btn-success"/>
      {feedback}
      </div>
    )
  }
}

class HiddenInput extends React.Component {
  // props:
    // formData : what formData[key] in Form.state.formData
    // name : field name
  render() {
    const valueLoaded = !!("value" in this.props.formData)

    // defaults
    let value;

    if (valueLoaded) {
      value = this.props.formData.value || "";
    } else {
      value = "";
    }

    <input 
      type="hidden"
      name={this.props.name} 
      value={value}
    />
  }
}

class TextInput extends React.Component {
  // props:
    // formData : what formData[key] in Form.state.formData
    // name : field name
    // moreClasses : more classes
    // errors: if there are errors to display

  render() {
    const optionsLoaded = !!("options" in this.props.formData)
    const valueLoaded = !!("value" in this.props.formData)

    // defaults
    let type;
    let placeholder;
    let className = "form-control" + (this.props.errors ? " is-invalid" : "");
    let value;
    let label;
    let helptext;
    let readOnly;

    if (optionsLoaded) {
      type = this.props.formData.options.type;
      placeholder = this.props.formData.options.react_meta.placeholder || null;
      label = this.props.formData.options.react_meta.label || this.props.formData.options.label;
      helptext = this.props.formData.options.react_meta.help_text || null;
      readOnly = this.props.formData.options.react_meta.read_only || false;
    } else {
      type = "text";
      placeholder = null;
      label = null;
      helptext = null;
      readOnly = false;
    }

    if (valueLoaded) {
      value = this.props.formData.value || "";
    } else {
      value = "";
    }
    
    return (
      <div className="form-group">
        <label htmlFor={this.props.name}>{label}</label>
        <input 
          readOnly={readOnly} 
          onChange={readOnly? null: this.props.onChange} 
          type={type} 
          name={this.props.name} 
          className={className} 
          placeholder={placeholder} 
          value={value}
        />
        <small className="form-text text-muted">{helptext}</small>
        <div className="invalid-feedback">
          {this.props.errors}
        </div>
      </div>
    )
  }
}