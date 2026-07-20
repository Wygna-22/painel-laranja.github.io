import "./DashboardLayout.css";

interface Props {
    children: React.ReactNode;
}

export default function DashboardLayout({ children }: Props) {
    return (
        <div className="dashboard-layout">
            {children}
        </div>
    );
}