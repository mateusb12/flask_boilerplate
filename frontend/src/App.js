import logo from './logo.svg';
import './App.css';
import {Routes, Route} from "react-router-dom";
import LoginForm from "./components/login/LoginForm";
import {QueryClient, QueryClientProvider} from "@tanstack/react-query";
// Create a client
const queryClient = new QueryClient();

function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <Routes>
                <Route path="/" element={<LoginForm/>}/>
            </Routes>
        </QueryClientProvider>
    );
}

export default App;
