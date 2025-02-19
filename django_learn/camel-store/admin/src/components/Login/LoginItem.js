import React, {Component} from 'react';
import {Form, Input, Row, Col, Spin} from 'antd';
import omit from 'omit.js';
import styles from './index.less';
import ItemMap from './map';
import LoginContext from './loginContext';

const FormItem = Form.Item;

class WrapFormItem extends Component {
    static defaultProps = {
        buttonText: '获取验证码',
    };

    constructor(props) {
        super(props);
        this.state = {
            count: 0,
            codeimg: ''
        };
    }

    componentDidMount() {
        const {updateActive, name} = this.props;
        if (updateActive) {
            updateActive(name);
        }
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    onGetCaptcha = () => {
        const {onGetchallenge} = this.props;
        if (onGetchallenge) {
            onGetchallenge()
        }
        // const result = onGetchallenge ? onGetchallenge() : null;
        // if (result === false) {
        //   return;
        // }
        // if (result instanceof Promise) {
        //   result.then(this.runGetCaptchaCountDown);
        // } else {
        //   this.runGetCaptchaCountDown();
        // }
    };

    getFormItemOptions = ({onChange, defaultValue, customprops, rules}) => {
        const options = {
            rules: rules || customprops.rules,
        };
        if (onChange) {
            options.onChange = onChange;
        }
        if (defaultValue) {
            options.initialValue = defaultValue;
        }
        return options;
    };

    runGetCaptchaCountDown = () => {
        const {countDown} = this.props;
        let count = countDown || 59;
        this.setState({count});
        this.interval = setInterval(() => {
            count -= 1;
            this.setState({count});
            if (count === 0) {
                clearInterval(this.interval);
            }
        }, 1000);
    };

    //获取焦点
    inputOnClick = () => {
        const {input} = this.inputRef;
        this.timer = setTimeout(() => {
            try {
                input.scrollIntoViewIfNeeded()
            } catch (e) {
                console.log('浏览器不支持scrollIntoViewIfNeeded')
            }
        }, 400);
    }
    //失去焦点
    inputOnBlur = () => {
        clearTimeout(this.timer)
    }

    render() {
        const {count} = this.state;

        const {
            form: {getFieldDecorator},
        } = this.props;

        // 这么写是为了防止restProps中 带入 onChange, defaultValue, rules props
        const {
            onChange,
            customprops,
            defaultValue,
            rules,
            name,
            buttonText,
            updateActive,
            codeLoading,
            type,
            codeimg,
            ...restProps
        } = this.props;

        // get getFieldDecorator props
        const options = this.getFormItemOptions(this.props);

        const otherProps = restProps || {};
        if (type === 'Captcha') {
            const inputProps = omit(otherProps, ['onGetCaptcha', 'countDown']);
            return (
                < FormItem
            className = {styles.getCaptcha} >
                < Row >
                < Col
            span = {17} >
                {getFieldDecorator(name, options)(
                < Input
            {...
                customprops
            }
            {...
                inputProps
            }
            ref = {(input)
        =>
            {
                this.inputRef = input;
            }
        }
            onClick = {this.inputOnClick}
            onBlur = {this.inputOnBlur}
            />)}
            < /Col>
            < Col
            span = {6} >
                < Spin
            spinning = {codeLoading} >
                < img
            alt = "Captcha"
            style = {
            {
                width:'100%', height
            :
                35, marginTop
            :
                -4, marginLeft
            :
                10
            }
        }
            onClick = {this.onGetCaptcha}
            src = {codeimg}
            />
            < /Spin>
            < /Col>
            < /Row>
            < /FormItem>
        )
            ;
        }
            return (
                < FormItem >
                {getFieldDecorator(name, options)(
                < Input
            {...
                customprops
            }
            {...
                otherProps
            }
            ref = {(input)
        =>
            {
                this.inputRef = input;
            }
        }
            onClick = {this.inputOnClick}
            onBlur = {this.inputOnBlur}
            />
        )
        }
        <
            /FormItem>
        )
            ;
        }
    }

    const
    LoginItem = {};
    Object
.

    keys(ItemMap)

.

    forEach(key

=> {
    const
    item = ItemMap[key];
    LoginItem
    [key] = props => (
        < LoginContext.Consumer >
        {context
=> (
<
    WrapFormItem
    customprops = {item.props}
    rules = {item.rules} {
...
    props
}

type = {key}
updateActive = {context.updateActive}
form = {context.form}
/>
)
}
<
/LoginContext.Consumer>
)
;
})
;

export default LoginItem;
