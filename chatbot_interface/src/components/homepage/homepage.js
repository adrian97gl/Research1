import ChatBot from 'react-simple-chatbot'
import { ThemeProvider } from 'styled-components';
import style from './style.css'

const theme = {
    background: '#f5f8fb',
    fontFamily: 'Helvetica Neue',
    headerBgColor: '#EF6C00',
    headerFontColor: '#fff',
    headerFontSize: '15px',
    botBubbleColor: '#EF6C00',
    botFontColor: '#fff',
    userBubbleColor: '#fff',
    userFontColor: '#4a4a4a',
};

const steps = [
    {
        id: '1',
        message: 'Hello World',
        // trigger: '2'
        end: true,
    },
];


function Homepage() {
    return (
        <div className={style.homepage}>
            <h1>Psihological chatbot</h1>
            <ThemeProvider theme={theme}>
                <ChatBot steps={steps}  />
            </ThemeProvider>
        </div>
    );
}

export default Homepage;
