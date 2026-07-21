import {
    LayoutDashboard,
    Users,
    CalendarDays,
    CalendarCheck,
    FileBarChart2,
    UserCog,
    ClipboardList,
    Activity,
    LogOut,
} from "lucide-react";

import { NavLink } from "react-router-dom";
import "./Sidebar.css";

export default function Sidebar() {
    return (
        <aside className="sidebar">

            <div className="logo">
                🍊 Painel Laranja
            </div>

            <nav>

                <NavLink to="/">
                    <LayoutDashboard size={20} />
                    Dashboard
                </NavLink>

                <NavLink to="/colaboradores">
                    <Users size={20} />
                    Colaboradores
                </NavLink>

                <NavLink to="/ferias">
                    <CalendarDays size={20} />
                    Férias
                </NavLink>

                <NavLink to="/folgas">
                    <CalendarCheck size={20} />
                    Folgas
                </NavLink>

                <NavLink to="/relatorios">
                    <FileBarChart2 size={20} />
                    Relatórios
                </NavLink>

                <NavLink to="/gestores">
                    <UserCog size={20} />
                    Gestores
                </NavLink>

                <NavLink to="/indicadores">
                    <Activity size={20}/>
                    Indicadores
                </NavLink>

                <NavLink to="/historico">
                    <ClipboardList size={20}/>
                    Histórico
                </NavLink>

            </nav>

            <div className="logout">

                <NavLink to="/login">
                    <LogOut size={20}/>
                    Sair
                </NavLink>

            </div>

        </aside>
    );
}