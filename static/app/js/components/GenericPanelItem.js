import React from 'react';
import {Panel, Label, Badge} from 'react-bootstrap';
import {Link} from 'react-router';
import {pure} from 'recompose';
 
const GenericPanelItem = React.createClass({render(){
    const margin = {
	marginLeft:'5px' 
    };
    console.log(this.props);
    const pk = this.props.pk;
    const uri = this.props.uri+ pk + '/';
    const fields = this.props.fields;
    const tags = fields.tags.map((label,i)=>(<Label key={i} bsStyle="info" style={margin}>{label}</Label>)); 
    const title = (<Link to={uri}>{fields.title}</Link>);
    return (
	    <Panel header={title} footer={tags} bsStyle={this.props.bsStyle}>
	    {fields.text}
	    <Link to={uri}>...</Link>
	</Panel> 
    );
}});

GenericPanelItem.propTypes = {
    pk:React.PropTypes.number,
    uri:React.PropTypes.string,
    fields:React.PropTypes.array,
    tags:React.PropTypes.array,
    bsStyle:React.PropTypes.string
};
    

export default pure(GenericPanelItem);















