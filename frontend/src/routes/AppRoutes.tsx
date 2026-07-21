import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import Dashboard from "../pages/Dashboard/Dashboard";
import Colaboradores from "../pages/Colaboradores/Colaboradores";
import Ferias from "../pages/Ferias/Ferias";
import Folgas from "../pages/Folgas/Folgas";
import Relatorios from "../pages/Relatorios/Relatorios";
import Login from "../pages/Login/Login";

import ProtectedRoute from "../components/ProtectedRoute";

export default function AppRoutes() {
    return (
        <BrowserRouter basename="/painel-laranja.github.io">

            <Routes>

                <Route
                    path="/"
                    element={<Navigate to="/login" replace />}
                />

                <Route
                    path="/login"
                    element={<Login />}
                />

                <Route
                    element={
                        <ProtectedRoute>
                            <MainLayout />
                        </ProtectedRoute>
                    }
                >

                    <Route
                        path="/dashboard"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/colaboradores"
                        element={<Colaboradores />}
                    />

                    <Route
                        path="/ferias"
                        element={<Ferias />}
                    />

                    <Route
                        path="/folgas"
                        element={<Folgas />}
                    />

                    <Route
                        path="/relatorios"
                        element={<Relatorios />}
                    />

                </Route>

            </Routes>

        </BrowserRouter>
    );
}