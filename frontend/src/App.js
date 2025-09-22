import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { AuthProvider, useAuth } from './contexts/AuthContext';

// Components
import Login from './components/auth/Login';
import Dashboard from './components/dashboard/Dashboard';
import Programs from './components/programs/Programs';
import Batches from './components/batches/Batches';
import Progress from './components/progress/Progress';
import Users from './components/users/Users';
import Layout from './components/layout/Layout';

// Create theme
const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
  },
});

// Protected Route component - can be used for future route protection
// const ProtectedRoute = ({ children }) => {
//   const { isAuthenticated, loading } = useAuth();
//
//   if (loading) {
//     return <div>Loading...</div>;
//   }
//
//   return isAuthenticated ? children : <Navigate to="/login" replace />;
// };

// Main App component
function AppRoutes() {
  const { isAuthenticated } = useAuth();

  return (
    <Router>
      <div className="App">
        {isAuthenticated ? (
          <Layout>
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/programs" element={<Programs />} />
              <Route path="/batches" element={<Batches />} />
              <Route path="/progress" element={<Progress />} />
              <Route path="/users" element={<Users />} />
              <Route path="/login" element={<Navigate to="/" replace />} />
            </Routes>
          </Layout>
        ) : (
          <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="*" element={<Navigate to="/login" replace />} />
          </Routes>
        )}
      </div>
    </Router>
  );
}

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AuthProvider>
        <AppRoutes />
      </AuthProvider>
    </ThemeProvider>
  );
}

export default App;
