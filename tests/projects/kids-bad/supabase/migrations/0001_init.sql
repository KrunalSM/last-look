create table public.children (
  id uuid primary key default gen_random_uuid(),
  child_name text not null,
  child_age int not null,
  school text,
  parent_email text not null,
  parental_consent boolean not null default false,
  consent_at timestamptz,
  created_at timestamptz not null default now()
);

alter table public.children enable row level security;
