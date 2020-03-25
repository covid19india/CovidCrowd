import React, {Component} from 'react';

export default class homePage extends Component {
  constructor(props) {
    super(props);
    this.data = [
        {
          id: 1,
          'Diagnosed data': '04/Mar/2020',
          'Detected state': 'AP',
          city: 'hyd',
          age: 20,
          gender: 'male',
          status: 'hosp',
          details: 'dffds'
        },
        {
          id: 0,
          'Diagnosed data': '04/Mar/2020',
          'Detected state': 'AP',
          city: 'hyd',
          age: 20,
          gender: 'male',
          status: 'hosp',
          details: 'dffds'
        },
        {
          id: 2,
          'Diagnosed data': '04/Mar/2020',
          'Detected state': 'AP',
          city: 'hyd',
          age: 20,
          gender: 'male',
          status: 'hosp',
          details: 'dffds'
        },
        {
          id: 4,
          'Diagnosed data': '04/Mar/2020',
          'Detected state': 'AP',
          city: 'hyd',
          age: 20,
          gender: 'male',
          status: 'hosp',
          details: 'dffds'
        },
        {
          id: 3,
          'Diagnosed data': '04/Mar/2020',
          'Detected state': 'AP',
          city: 'hyd',
          age: 20,
          gender: 'male',
          status: 'hosp',
          details: 'dffds'
        },
        {
          id: 10,
          'Diagnosed data': '04/Mar/2020',
          'Detected state': 'AP',
          city: 'hyd',
          age: 20,
          gender: 'male',
          status: 'hosp',
          details: 'dffds'
        },
      ];
    this.state = {
      format: {
        class: {
          id: "orderable",
          'Diagnosed data': 'desc orderable',
          'Detected state': 'orderable',
          city: 'orderable',
          age: 'orderable',
          gender: 'orderable',
          status: 'orderable',
          details: ''
        }
      },
      filterVisible: false
    };
    this.handleFilterClick = this.handleFilterClick.bind(this);
  }

  handleFilterClick(event) {
    this.setState({filterVisible: !this.state.filterVisible})
  }

  render() {
    return (
      <div className="container">
        <div className="row mt-3 mb-3">
          <div className="col">
            <h4 className="h4 text-uppercase">Affected People</h4>
          </div>
          <div className="col">
            <button id="show-filters" className="btn btn-default float-right" onClick={this.handleFilterClick}>
              <i className="fa fa-filter"/>
              <span id="fBtnText">Filters</span>
            </button>
          </div>
        </div>
        <div className="row py-2">
          <div className="col">
            <div className="alert alert-info">
              <i className="fa fa-info-circle"/> If you find any errors in the data here. Kindly
              use the <strong>Report Error</strong> option in the details page of the
              patient.
            </div>
          </div>
        </div>
        {this.state.filterVisible ?
          <div id="filter-container">
            <form className="form-horizontal" method="get">
              <div id="div_id_diagnosed_date" className="form-group row row"><label htmlFor="id_diagnosed_date"
                                                                                    className="col-form-label col-md-2">
                Diagnosed date
              </label>
                <div className="col-md-10"><input type="text" name="diagnosed_date" value="03/04/2020"
                                                  className="dateinput form-control" id="id_diagnosed_date"/></div>
              </div>
              <div id="div_id_detected_state" className="form-group row row"><label htmlFor="id_detected_state"
                                                                                    className="col-form-label col-md-2">
                Detected state
              </label>
                <div className="col-md-10"><select name="detected_state" className="select form-control"
                                                   id="id_detected_state">
                  <option value="" selected="">---------</option>
                  <option value="Andaman and Nicobar Islands">Andaman and Nicobar Islands</option>
                  <option value="Andhra Pradesh">Andhra Pradesh</option>
                  <option value="Assam">Assam</option>
                  <option value="Bihar">Bihar</option>
                  <option value="Chandigarh">Chandigarh</option>
                  <option value="Chattisgarh">Chattisgarh</option>
                  <option value="Dadar and Nagar Haveli">Dadar and Nagar Haveli</option>
                  <option value="Daman and Diu">Daman and Diu</option>
                  <option value="Delhi">Delhi</option>
                  <option value="Goa">Goa</option>
                  <option value="Gujarat">Gujarat</option>
                  <option value="Haryana">Haryana</option>
                  <option value="Himachal Pradesh">Himachal Pradesh</option>
                  <option value="Jammu and Kashmir">Jammu and Kashmir</option>
                  <option value="Jharkhand">Jharkand</option>
                  <option value="Karnataka">Karnataka</option>
                  <option value="Kerala">Kerala</option>
                  <option value="Ladakh">Ladakh</option>
                  <option value="Lakshadweep">Lakshadweep</option>
                  <option value="Madhya Pradesh">Madhya Pradesh</option>
                  <option value="Maharashtra">Maharashtra</option>
                  <option value="Manipur">Manipur</option>
                  <option value="Meghalaya">Meghalaya</option>
                  <option value="Mizoram">Mizoram</option>
                  <option value="Nagaland">Nagaland</option>
                  <option value="Delhi">Delhi</option>
                  <option value="Odisha">Odisha</option>
                  <option value="Puducherry">Puducherry</option>
                  <option value="Punjab">Punjab</option>
                  <option value="Rajasthan">Rajasthan</option>
                  <option value="Sikkim">Sikkim</option>
                  <option value="Tamil Nadu">Tamil Nadu</option>
                  <option value="Telangana">Telangana</option>
                  <option value="Tripura">Tripura</option>
                  <option value="Uttar Pradesh">Uttar Pradesh</option>
                  <option value="Uttarakhand">Uttarakhand</option>
                  <option value="West Bengal">West Bengal</option>

                </select></div>
              </div>
              <div id="div_id_detected_city" className="form-group row row"><label htmlFor="id_detected_city"
                                                                                   className="col-form-label col-md-2">
                Detected city
              </label>
                <div className="col-md-10"><input type="text" name="detected_city"
                                                  className="textinput textInput form-control" id="id_detected_city"/>
                </div>
              </div>
              <div id="div_id_gender" className="form-group row row"><label htmlFor="id_gender"
                                                                            className="col-form-label col-md-2">
                Gender
              </label>
                <div className="col-md-10"><select name="gender" className="select form-control" id="id_gender">
                  <option value="" selected="">---------</option>
                  <option value="Male">Male</option>
                  <option value="Female">Female</option>
                  <option value="Others">Others</option>
                  <option value="Unknown">Unknown</option>

                </select></div>
              </div>
              <div id="div_id_current_status" className="form-group row row"><label htmlFor="id_current_status"
                                                                                    className="col-form-label col-md-2">
                Current status
              </label>
                <div className="col-md-10"><select name="current_status" className="select form-control"
                                                   id="id_current_status">
                  <option value="" selected="">---------</option>
                  <option value="Hospitalized">Hospitalized</option>
                  <option value="Recovered">Recovered</option>
                  <option value="Deceased">Deceased</option>
                  <option value="Home Quarantined">Home Quarantined</option>

                </select></div>
              </div>
              <div className="form-group row">
                <div className="aab col-md-2"></div>
                <div className="col-md-10"><input type="submit" name="submit" value="Apply Filters"
                                                  className="btn btn-primary" id="submit-id-submit"/></div>
              </div>
            </form>
          </div>
          : null
          }
        <div className="table-container">
          <table className="table table-responsive">
            <thead>
            <tr>
              {Object.keys(this.data[0]).map((i, k) => {
                return (
                  <th className={this.state.format.class[i]}>
                    <b>{i} </b>
                  </th>
                )
              })}
            </tr>
            </thead>
            <tbody>
            {this.data.map((dt, i) => {
              return (
                <tr>
                  {Object.keys(dt).map((key, ind) => (
                      <td>{dt[key]}</td>
                    )
                  )}
                </tr>
              )
            })}
            </tbody>
          </table>
        </div>
        <p className="text-right">
          <small>
            <strong>Download </strong>

            <span className="ml-2">
        <a
          href="/export?diagnosed_date=03%2F04%2F2020&amp;detected_state=&amp;detected_city=&amp;gender=&amp;current_status=&amp;submit=Apply+Filters&amp;_export=csv">
          <code>CSV</code>
        </a>
     </span>

            <span className="ml-2">
        <a
          href="/export?diagnosed_date=03%2F04%2F2020&amp;detected_state=&amp;detected_city=&amp;gender=&amp;current_status=&amp;submit=Apply+Filters&amp;_export=json">
          <code>JSON</code>
        </a>
     </span>

            <span className="ml-2">
        <a
          href="/export?diagnosed_date=03%2F04%2F2020&amp;detected_state=&amp;detected_city=&amp;gender=&amp;current_status=&amp;submit=Apply+Filters&amp;_export=latex">
          <code>LATEX</code>
        </a>
     </span>

            <span className="ml-2">
        <a
          href="/export?diagnosed_date=03%2F04%2F2020&amp;detected_state=&amp;detected_city=&amp;gender=&amp;current_status=&amp;submit=Apply+Filters&amp;_export=tsv">
          <code>TSV</code>
        </a>
     </span>

          </small>
        </p>
      </div>
    )
  }
}